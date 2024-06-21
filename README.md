# Загрузчик постов из группы VK

Этот Python-скрипт загружает все посты со стены указанной группы VK с использованием VK API.

## Предварительные требования

- Python 3.x
- Библиотека `requests`

Вы можете установить необходимую библиотеку с помощью pip:
```sh
pip install requests
```

## Получение токена доступа VK

Для использования этого скрипта вам понадобится токен доступа VK. Следуйте этим шагам, чтобы его получить:

1. **Создайте приложение VK**:
   - Перейдите на [страницу создания приложений VK](https://dev.vk.com/ru/admin/apps-list).
   - Создайте новое приложение. Вы получите `client_id`, который является ID вашего приложения.

2. **Создайте токен доступа**:
   - Откройте ваш браузер и перейдите по следующему URL, заменив `YOUR_APP_ID` на ID вашего приложения:
     ```
     https://oauth.vk.com/authorize?client_id=YOUR_APP_ID&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.21
     ```
   - Следуйте инструкциям, чтобы авторизовать приложение и получить токен доступа из URL, на который вы будете перенаправлены.

**Примечание**: Возможно, при использовании этого метода возникнут некоторые проблемы. Используйте его на свой страх и риск. Это метод, который сработал для меня.

## Использование

Чтобы загрузить все посты из группы VK с указанным доменом, используйте следующую команду:

```sh
python main.py --access_token YOUR_ACCESS_TOKEN --domain DOMAIN
```

- `YOUR_ACCESS_TOKEN`: Токен доступа, который вы получили на предыдущем шаге.
- `DOMAIN`: Короткий адрес группы VK (без `vk.com/`).

После выполнения команды будет создан файл `wall_posts.json`. Запустите `python parser.py`, чтобы распарсить данные из него, или используйте свой собственный парсер для этой задачи. `parser.py` является примером инструмента, который может парсить фото, музыку, документы и генерировать посты в читаемом формате. Все остальные вложения будут включены как JSON-блоки. `parser.py` также создает файл, содержащий все прямые ссылки на файлы. Например, если вы хотите загрузить все фото, вы можете использовать список ссылок, сгенерированных скриптом.

### Пример

1. Загрузите все посты из группы с доменом `example_group`:
   ```sh
   python main.py --access_token YOUR_ACCESS_TOKEN --domain example_group
   ```
2. Запустите парсер для обработки загруженных данных:
   ```sh
   python parser.py
   ```

## Кастомизация

Не стесняйтесь модифицировать скрипт, если вам нужно использовать больше параметров или использовать ID вместо домена. Для получения дополнительной информации о дополнительных параметрах и методах, обратитесь к [официальной документации VK API](https://dev.vk.com/ru/method/wall.get).

## Лицензия

Этот проект лицензирован по лицензии MIT.

# VK Group Wall Downloader

This Python script downloads all posts from a specified VK group wall using the VK API.

## Prerequisites

- Python 3.x
- `requests` library

You can install the required library using pip:
```sh
pip install requests
```

## Getting Your VK Access Token

To use this script, you need a VK access token. Follow these steps to obtain one:

1. **Create a VK App**:
   - Go to the [VK App Creation Page](https://dev.vk.com/ru/admin/apps-list).
   - Create a new app. You will receive a `client_id`, which is the ID of your app.

2. **Generate Access Token**:
   - Open your browser and run the following URL, replacing `YOUR_APP_ID` with your app's ID:
     ```
     https://oauth.vk.com/authorize?client_id=YOUR_APP_ID&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.21
     ```
   - Follow the instructions to authorize the app and obtain the access token from the URL you are redirected to.

**Note**: There might be some issues with this method. Use it at your own risk. This is the method that worked for me.

## Usage

To download all posts from a VK group with a specified domain, use the following command:

```sh
python main.py --access_token YOUR_ACCESS_TOKEN --domain DOMAIN
```

- `YOUR_ACCESS_TOKEN`: The access token you obtained in the previous step.
- `DOMAIN`: The short address of the VK group (without `vk.com/`).

After that, the `wall_posts.json` file will be created. Run `python parser.py` to parse data from it, or use your own parser to do that. `parser.py` is an example tool that can parse photos, music, documents, and generate posts in a readable format. All other attachments will be included as JSON blocks. `parser.py` also creates a file that includes all direct links to files. For example, if you want to download all photos, you can use the list of links generated by the script.

### Example

1. Download all posts from the group with the domain `example_group`:
   ```sh
   python main.py --access_token YOUR_ACCESS_TOKEN --domain example_group
   ```
2. Run the parser to process the downloaded data:
   ```sh
   python parser.py
   ```

## Customization

Feel free to modify the script if you want to use more parameters or use an ID instead of a domain. For more information on additional parameters and methods, refer to the [official VK API documentation](https://dev.vk.com/ru/method/wall.get).

## License

This project is licensed under the MIT License.