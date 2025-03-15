import qrcode

class Simple_QR:
    def __init__(self,size: int, padding: int):
        self.qr = qrcode.QRCode(box_size=size,border=padding)

    def create_qr(self, file_name: str, fg: str, bg: str):
        user_input: str = input("Enter text: ")

        try:
            self.qr.add_data(user_input)
            qr_image = self.qr.make_image(fill_color=fg, back_color=bg)
            qr_image.save(file_name)

            print(f"Successfully created! ({file_name})")

        except Exception as e:
            print(f"Error: {e}")


def main():
    simple_qr = Simple_QR(size=30, padding=2)
    simple_qr.create_qr("qr_sample.png",fg="black",bg="white")


if __name__ == "__main__":
    main()

