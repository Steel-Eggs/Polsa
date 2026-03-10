# Agent Bootstrap Checklist (Sputnik baseline)

Цель: быстро развернуть нового ассистента (как для проекта СПУТНИК), не теряя времени на поиски конфигов.

## 1. Первичная персонализация
1. **Файлы:** `IDENTITY.md`, `USER.md`.
2. **Что спросить у владельца:**
   - Имя, как обращаться, место/часовой пояс.
   - Семью, ключевые даты (дни рождения), адрес (если нужно для контекста).
   - Приоритеты (основные проекты, цели, табу).
   - Границы по внешним действиям (можно ли публиковать/писать от имени без разрешения?).
3. **Что сделать:**
   - Заполнить `IDENTITY.md` (имя ассистента, вайб, эмодзи, аватар).
   - Заполнить `USER.md` (контакты, семья, бизнес, приоритеты, правила).
   - Создать/обновить `memory/YYYY-MM-DD.md` с кратким журналом дня.
   - Удалить `BOOTSTRAP.md`, когда настройка завершена.

## 2. Доступ к терминалу / инструментам
1. **Цель:** включить `exec`, `process`, `read/write` и управление подагентами (tmux, sessions_spawn).
2. **Config:** файл `~/.openclaw/openclaw.json`.
3. **Шаги:**
   - Убедиться, что существует блок `tools`.
   - Включить обмен агентами:
     ```json5
     "tools": {
       "agentToAgent": { "enabled": true },
       ...
     }
     ```
   - Сменить профиль инструментов на «coding» или «full»:
     ```bash
     openclaw config set tools.profile "full"
     ```
     | Profile | Что включает |
     | ------- | ------------ |
     | minimal | только `session_status` |
     | messaging | `message` + сессии |
     | coding | `group:fs`, `group:runtime`, `group:sessions`, `group:memory`, `image` |
     | full | все инструменты |
   - Перезапустить: `openclaw gateway restart`.
4. **Проверка:**
   - `exec{"command":"pwd"}` возвращает `workspace`.
   - `sessions_list` / `sessions_spawn` доступны.

## 3. Голос / ElevenLabs TTS
1. **Найти и установить скилл:**
   ```bash
   clawhub search elevenlabs
   clawhub install openclaw-skill-elevenlabs-pro --force  # предварительно просмотреть код
   ```
2. **Подключить API-ключ:**
   - Сгенерировать ключ с правами `user_read`, `voices_read`, `speech_synthesis`.
   - Сохранить в `~/.openclaw/.env` (файл не коммитится):
     ```bash
     cat <<'EOF' > ~/.openclaw/.env
     ELEVENLABS_API_KEY=sk_...
     EOF
     ```
   - Перед запуском команд экспортировать переменную: `set -a && . ~/.openclaw/.env && set +a`.
   - Если API отвечает `missing_permissions`, попросить владельца пересоздать ключ с нужными правами.
3. **Подбор голоса:**
   - Прослушать предпросмотры (пример: River https://storage.googleapis.com/eleven-public-prod/premade/voices/SAz9YHcvj6GT2YYXdXww/e6c95f0b-2227-491a-b3d7-2249240decb7.mp3).
   - Команда для списка голосов и ссылок:
     ```bash
     python3 skills/openclaw-skill-elevenlabs-pro/scripts/elevenlabs.py --list-voices --json | less
     ```
   - Генерация тестового файла:
     ```bash
     python3 skills/openclaw-skill-elevenlabs-pro/scripts/elevenlabs.py "Текст" \
       --voice "River" --model eleven_multilingual_v2 \
       --stability 0.8 --similarity 0.7 --style 0.9 \
       --output media/tts/<имя>.mp3
     ```
   - **Текущий дефолт для Антона:** Voice River (ID `SAz9YHcvj6GT2YYXdXww`), `eleven_multilingual_v2`, stability 0.8, similarity 0.7, style 0.9, speaker boost включён.

## 5. (Резерв) новые настройки
- Каждую новую интеграцию описываем отдельным подразделом (что установить, какой конфиг, какие команды).
- Формат: *шаг → подзадачи → команды/файлы → проверка.*

_Последнее обновление: 2026-03-04 (Польза)._ 

## 4. Веб-поиск (Brave Search API)
1. **Получить API key:**
   - Зарегистрироваться на https://brave.com/search/api/ (потребуется карта, но ежемесячно дают $5 бесплатных кредитов).
   - Скопировать ключ формата `BSA0-...`.
2. **Прописать ключ в конфиге:**
   ```bash
   openclaw config set tools.web.search.apiKey "<BRAVE_API_KEY>"
   ```
   (Дополнительно можно держать копию в `~/.openclaw/.env` как `BRAVE_API_KEY=...`).
3. **Перезапустить gateway:** `openclaw gateway restart`.
4. **Проверка:** `web_search {"query":"пример"}` должно вернуть результаты Brave.

_Текущий ключ (март 2026): `BSA0-ydkBBsAiN-cvt0MbECGBKAN8A_`._
