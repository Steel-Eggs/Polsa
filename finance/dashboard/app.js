(() => {
  const formatter = new Intl.NumberFormat('ru-RU', {
    style: 'currency',
    currency: 'RUB',
    maximumFractionDigits: 2
  });

  const rawData = (window.EXPENSE_DATA || []).map((entry) => {
    const dateStr = entry.date || null;
    const dateObj = dateStr ? new Date(`${dateStr}T00:00:00`) : null;
    const amount = typeof entry.line_total_rub === 'number' ? entry.line_total_rub : 0;
    return {
      ...entry,
      dateObj,
      amount
    };
  });

  const spendData = rawData.filter((item) => item.category && item.category !== 'Инфо');
  const infoData = rawData.filter((item) => item.category === 'Инфо');

  const elements = {
    category: document.getElementById('categoryFilter'),
    subcategory: document.getElementById('subcategoryFilter'),
    dateFrom: document.getElementById('dateFrom'),
    dateTo: document.getElementById('dateTo'),
    search: document.getElementById('searchFilter'),
    reset: document.getElementById('resetFilters'),
    summary: document.getElementById('summary'),
    tableBody: document.getElementById('tableBody'),
    tableInfo: document.getElementById('tableInfo'),
    lastUpdated: document.getElementById('lastUpdated')
  };

  let weeklyChart;
  let monthlyChart;

  function formatDate(dateObj) {
    if (!dateObj) return '—';
    return dateObj.toLocaleDateString('ru-RU', {
      day: '2-digit',
      month: '2-digit',
      year: 'numeric'
    });
  }

  function initFilters() {
    const categories = Array.from(new Set(spendData.map((item) => item.category).filter(Boolean))).sort();
    categories.forEach((cat) => {
      const option = document.createElement('option');
      option.value = cat;
      option.textContent = cat;
      elements.category.appendChild(option);
    });
    updateSubcategories();
  }

  function updateSubcategories() {
    const currentCategory = elements.category.value;
    const target = currentCategory
      ? spendData.filter((item) => item.category === currentCategory)
      : spendData;
    const subcategories = Array.from(new Set(target.map((item) => item.subcategory).filter(Boolean))).sort();
    elements.subcategory.innerHTML = '<option value="">Все</option>';
    subcategories.forEach((sub) => {
      const option = document.createElement('option');
      option.value = sub;
      option.textContent = sub;
      elements.subcategory.appendChild(option);
    });
  }

  function applyFilters() {
    const category = elements.category.value;
    const subcategory = elements.subcategory.value;
    const searchTerm = elements.search.value.trim().toLowerCase();
    const fromDate = elements.dateFrom.value ? new Date(`${elements.dateFrom.value}T00:00:00`) : null;
    const toDate = elements.dateTo.value ? new Date(`${elements.dateTo.value}T23:59:59`) : null;

    return spendData.filter((item) => {
      if (category && item.category !== category) return false;
      if (subcategory && item.subcategory !== subcategory) return false;
      if (fromDate && item.dateObj && item.dateObj < fromDate) return false;
      if (toDate && item.dateObj && item.dateObj > toDate) return false;
      if (searchTerm) {
        const haystack = `${item.vendor || ''} ${item.item || ''} ${item.notes || ''}`.toLowerCase();
        if (!haystack.includes(searchTerm)) return false;
      }
      return true;
    });
  }

  function renderSummary(data) {
    const total = data.reduce((sum, item) => sum + item.amount, 0);
    const positions = data.length;
    const categories = new Set(data.map((item) => item.category));
    const receipts = new Set(data.map((item) => item.receipt_id).filter(Boolean));

    const dates = data.filter((item) => item.dateObj).sort((a, b) => a.dateObj - b.dateObj);
    const period = dates.length ? `${formatDate(dates[0].dateObj)} → ${formatDate(dates[dates.length - 1].dateObj)}` : 'Нет данных';

    const discount = infoData.reduce((sum, row) => {
      if (!row.notes) return sum;
      const matches = row.notes.match(/([0-9]+[\.,][0-9]+)/g) || [];
      const parsed = matches
        .map((m) => Number(m.replace(',', '.')))
        .filter((num) => !Number.isNaN(num));
      return sum + (parsed[0] || 0);
    }, 0);

    elements.summary.innerHTML = `
      <div class="card">
        <span>Всего по выборке</span>
        <strong>${formatter.format(total)}</strong>
      </div>
      <div class="card">
        <span>Позиции · чеки</span>
        <strong>${positions} / ${receipts.size}</strong>
      </div>
      <div class="card">
        <span>Категорий</span>
        <strong>${categories.size}</strong>
      </div>
      <div class="card">
        <span>Инфо</span>
        <strong>Скидки: ${discount ? formatter.format(discount) : '—'}</strong>
      </div>
      <div class="card">
        <span>Период выборки</span>
        <strong>${period}</strong>
      </div>
    `;

    const latest = data
      .filter((item) => item.dateObj)
      .sort((a, b) => b.dateObj - a.dateObj)[0];
    elements.lastUpdated.textContent = latest
      ? `Последняя запись: ${formatDate(latest.dateObj)}`
      : 'Нет активных записей';
  }

  function renderTable(data) {
    const rows = data
      .sort((a, b) => (b.dateObj || 0) - (a.dateObj || 0))
      .map((item) => {
        return `
          <tr>
            <td>${formatDate(item.dateObj)}</td>
            <td>${item.vendor || '—'}</td>
            <td>${item.category || '—'}</td>
            <td>${item.subcategory || '—'}</td>
            <td>${item.item || '—'}</td>
            <td>${formatter.format(item.amount)}</td>
            <td>${item.notes || ''}</td>
          </tr>
        `;
      })
      .join('');

    elements.tableBody.innerHTML = rows || `<tr><td colspan="7">Нет данных для отображения</td></tr>`;

    const total = data.reduce((sum, item) => sum + item.amount, 0);
    const receipts = new Set(data.map((item) => item.receipt_id).filter(Boolean));
    elements.tableInfo.textContent = `${data.length} позиций · ${receipts.size} чек(ов) · ${formatter.format(total)}`;
  }

  function getISOWeek(date) {
    const tmp = new Date(Date.UTC(date.getFullYear(), date.getMonth(), date.getDate()));
    const dayNum = tmp.getUTCDay() || 7;
    tmp.setUTCDate(tmp.getUTCDate() + 4 - dayNum);
    const yearStart = new Date(Date.UTC(tmp.getUTCFullYear(), 0, 1));
    const weekNo = Math.ceil(((tmp - yearStart) / 86400000 + 1) / 7);
    return { year: tmp.getUTCFullYear(), week: weekNo };
  }

  function aggregateByWeek(data) {
    const map = new Map();
    data.forEach((item) => {
      if (!item.dateObj) return;
      const { year, week } = getISOWeek(item.dateObj);
      const key = `${year}-W${String(week).padStart(2, '0')}`;
      map.set(key, (map.get(key) || 0) + item.amount);
    });
    return Array.from(map.entries()).sort(([a], [b]) => (a > b ? 1 : -1));
  }

  function aggregateByMonth(data) {
    const map = new Map();
    data.forEach((item) => {
      if (!item.dateObj) return;
      const key = `${item.dateObj.getFullYear()}-${String(item.dateObj.getMonth() + 1).padStart(2, '0')}`;
      map.set(key, (map.get(key) || 0) + item.amount);
    });
    return Array.from(map.entries()).sort(([a], [b]) => (a > b ? 1 : -1));
  }

  function updateCharts(data) {
    const weekly = aggregateByWeek(data);
    const monthly = aggregateByMonth(data);

    const weeklyCtx = document.getElementById('weeklyChart');
    const monthlyCtx = document.getElementById('monthlyChart');

    if (weeklyChart) weeklyChart.destroy();
    if (monthlyChart) monthlyChart.destroy();

    weeklyChart = new Chart(weeklyCtx, {
      type: 'bar',
      data: {
        labels: weekly.map(([label]) => label),
        datasets: [
          {
            label: 'Сумма',
            data: weekly.map(([, value]) => value),
            backgroundColor: '#2563eb'
          }
        ]
      },
      options: {
        scales: {
          y: {
            ticks: {
              callback: (value) => formatter.format(value)
            }
          }
        },
        plugins: {
          legend: { display: false }
        }
      }
    });

    monthlyChart = new Chart(monthlyCtx, {
      type: 'line',
      data: {
        labels: monthly.map(([label]) => label),
        datasets: [
          {
            label: 'Сумма',
            data: monthly.map(([, value]) => value),
            borderColor: '#14b8a6',
            backgroundColor: 'rgba(20, 184, 166, 0.2)',
            fill: true,
            tension: 0.3
          }
        ]
      },
      options: {
        scales: {
          y: {
            ticks: {
              callback: (value) => formatter.format(value)
            }
          }
        },
        plugins: {
          legend: { display: false }
        }
      }
    });
  }

  function refreshView() {
    const filtered = applyFilters();
    renderSummary(filtered);
    renderTable(filtered);
    updateCharts(filtered);
  }

  elements.category.addEventListener('change', () => {
    updateSubcategories();
    refreshView();
  });

  ['subcategory', 'dateFrom', 'dateTo'].forEach((key) => {
    elements[key].addEventListener('change', refreshView);
  });

  elements.search.addEventListener('input', () => {
    window.clearTimeout(elements.search._debounce);
    elements.search._debounce = window.setTimeout(refreshView, 250);
  });

  elements.reset.addEventListener('click', () => {
    elements.category.value = '';
    elements.subcategory.value = '';
    elements.dateFrom.value = '';
    elements.dateTo.value = '';
    elements.search.value = '';
    updateSubcategories();
    refreshView();
  });

  initFilters();
  refreshView();
})();
