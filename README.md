# International_TelegramBot

### It is a simple bot with i18n technology, which knows English and Russian at the moment.

## Tutorial

### Run project:

- Clone this repository to your remote server with the
  command `git clone https://github.com/BTMAN1489-1/International_TelegramBot.git`;
- Go to the project folder with the command `cd International_TelegramBot`;
- Compile .mo files based on .po files with the command `pybabel compile -d locales -D internatbot`;
- Run project with the command `python app.py` for Windows system or `python3 app.py` for others;

### Add new localizations:

- Create a .po file for the given language with the
  command `pybabel init -i locales/internatbot.pot -d locales -D internatbot -l <language>`;
- Make the translation in .po files you create with the following syntax:
    ```    
    msgid "<translatable English string>"
    msgstr "<the translated string into the desired language>"
  ```
- Compile .mo files based on .po files you created with the command `pybabel compile -d locales -D internatbot`;

### Update existing localizations:

- In the .pot file add the English string you want to translate with the following syntax:
    ```
    msgid "<translatable English string>"
    msgstr ""
  ```
- Update .po files with new translatable strings from the .pot file with the command `pybabel update -d locales -D internatbot -i locales/internatbot.pot`;
- Compile .mo files based on updated .po files with the command `pybabel compile -d locales -D internatbot`;