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

## What You Get

You will get a JSON file containing [all the post information](https://dev.vk.com/ru/reference/objects/post). The most important properties are:
- `"text"`: The content of the post.
- `"date"`: The timestamp of the post.
- `"attachments"`: An array containing attachments such as photos, etc.

Parsing all this data is up to you, depending on what you want to extract. In my case, I mostly look for text and date information, getting that is trivial, but you might need more information.

You can convert this JSON file to Excel using [this tool](https://www.convertcsv.com/json-to-csv.htm). Keep in mind, that it would not look well for posts with attachements. It's better to [parse them properly first](https://dev.vk.com/ru/reference/objects/attachments-wall).

To work with `"date"` timestamps, check [this tool](https://www.epochconverter.com/).

## Customization

Feel free to modify the script if you want to use more parameters or use an ID instead of a domain. For more information on additional parameters and methods, refer to the [official VK API documentation](https://dev.vk.com/ru/method/wall.get).

## License

This project is licensed under the MIT License.

# (RU) VK Group Wall Downloader

Этот Python-скрипт загружает все посты со стены указанной группы VK, используя VK API.

## Необходимые библиотеки

- Python 3.x
- Библиотека `requests`

Вы можете установить необходимую библиотеку, используя pip:
```sh
pip install requests
```

## Получение вашего VK Access Token

Чтобы использовать этот скрипт, вам нужен VK access token. Следуйте этим шагам, чтобы получить его:

1. **Создайте приложение VK**:
   - Перейдите на [страницу создания приложений VK](https://dev.vk.com/ru/admin/apps-list).
   - Создайте новое приложение. Вы получите `client_id`, который является ID вашего приложения.

2. **Создайте Access Token**:
   - Откройте браузер и выполните следующий URL, заменив `YOUR_APP_ID` на ID вашего приложения:
     ```
     https://oauth.vk.com/authorize?client_id=YOUR_APP_ID&display=page&redirect_uri=https://oauth.vk.com/blank.html&response_type=token&v=5.21
     ```
   - Следуйте инструкциям для авторизации приложения и получения access token из URL, на который вы будете перенаправлены.

**Примечание**: Могут возникнуть проблемы с этим методом. Используйте его на свой страх и риск. Это метод, который сработал для меня.

## Использование

Чтобы скачать все посты из группы VK с указанным доменом, используйте следующую команду:

```sh
python main.py --access_token YOUR_ACCESS_TOKEN --domain DOMAIN
```

- `YOUR_ACCESS_TOKEN`: Токен доступа, который вы получили на предыдущем шаге.
- `DOMAIN`: Краткий адрес группы VK (без `vk.com/`).

## Что вы получите

Вы получите JSON файл, содержащий [всю информацию о постах](https://dev.vk.com/ru/reference/objects/post). Наиболее важные свойства:
- `"text"`: Содержание поста.
- `"date"`: Таймстамп поста.
- `"attachments"`: Массив, содержащий вложения, такие как фотографии и т.д.

Парсинг всех этих данных зависит от вас, в зависимости от того, что вы хотите извлечь. В моем случае, я в основном ищу текст и информацию о дате, получение этого тривиально, но вам может понадобиться больше информации.

Вы можете конвертировать этот JSON файл в Excel, используя [этот инструмент](https://www.convertcsv.com/json-to-csv.htm). Имейте в виду, что это будет выглядеть не очень хорошо для постов с вложениями. Лучше [сначала правильно распарсить их](https://dev.vk.com/ru/reference/objects/attachments-wall).

Чтобы работать с таймстампами `"date"`, посмотрите [этот инструмент](https://www.epochconverter.com/).

## Настройка

Не стесняйтесь изменять скрипт, если вы хотите использовать больше параметров или использовать ID вместо домена. Для получения дополнительной информации о дополнительных параметрах и методах, обратитесь к [официальной документации VK API](https://dev.vk.com/ru/method/wall.get).

## Лицензия

Этот проект лицензирован по лицензии MIT.
