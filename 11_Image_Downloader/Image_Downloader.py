import os
import requests


def get_extension(image_url: str) -> str | None:
    extensions: list[str] = ['.png', '.jpg', '.svg', '.jpeg', '.gif']

    for ext in extensions:
        if ext in image_url:
            return ext


def download_image(image_url: str, name: str, folder: str):
    if ext := get_extension(image_url):
        if folder:
            image_name: str = f"{folder}/{name}{ext}"
        else:
            image_name: str = f"{name}{ext}"
    else:
        raise Exception("Image Could Not be loaded.")

    #checking if image already exists
    if os.path.isfile(image_name):
        raise Exception("Image already exists.")

    #downloading image
    try:
        image_content: bytes = requests.get(image_url).content
        with open(image_name, "wb") as handler:
            handler.write(image_content)
            print(f"User downloaded file: {image_name} Successfully")
    except Exception as e:
        print(f"Error: {e}")


def main() -> None:
    input_url: str = input("Enter Image URL: ")
    img_name: str = input("Enter image name: ")

    print("Downloading...")
    #print(get_extension("https://dragonball.fandom.com/wiki/Goku?file=Goku+anime+profile.png"))
    download_image(image_url=input_url,name=img_name,folder='Images')

if __name__ == "__main__":
    main()





