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

## Customization

Feel free to modify the script if you want to use more parameters or use an ID instead of a domain. For more information on additional parameters and methods, refer to the [official VK API documentation](https://dev.vk.com/ru/method/wall.get).

## License

This project is licensed under the MIT License.
