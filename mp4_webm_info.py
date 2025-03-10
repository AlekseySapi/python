import os
import subprocess
import json

line = '\n####### ####### ####### ####### #######'


def get_video_info(file):
    """Возвращает информацию о кодеке, битрейте и параметрах видеофайла."""
    try:
        result = subprocess.run(
            ["ffprobe", "-v", "quiet", "-print_format", "json", "-show_streams", file],
            capture_output=True,
            text=True,
            check=True,
        )
        data = json.loads(result.stdout)
        video_stream = next((stream for stream in data["streams"] if stream["codec_type"] == "video"), None)

        if not video_stream:
            print("\n⚠️  Видео поток не найден.\n")
            return None

        codec = video_stream.get("codec_name", "Неизвестно")
        bitrate = int(video_stream.get("bit_rate", 0)) // 1000 if "bit_rate" in video_stream else "Не указано"
        width = video_stream.get("width", "Неизвестно")
        height = video_stream.get("height", "Неизвестно")

        return {
            " Кодек": codec,
            " Битрейт (кбит/с)": bitrate,
            " Разрешение": f"{width}x{height}",
        }
    except Exception as e:
        print(f"\n⚠️  Ошибка при анализе: {e}\n")
        return None


def main():
    print(line)
    print("   < Анализ видеофайла [MP4/WebM] >\n")
    while True:
        print(line)
        file = input("# Введите имя файла:\n> ")

        if not os.path.isfile(file):
            print("\n⚠️  Файл не найден.")
            continue

        filename, ext = os.path.splitext(file)
        if ext.lower() not in ('.mp4', '.webm'):
            print("\n⚠️  Ошибка: Неверный формат файла.\n")
            continue

        info = get_video_info(file)
        if info:
            print("\n\n✅ Информация о видеофайле:")
            for key, value in info.items():
                print(f"{key}: {value}")
        print()


if __name__ == "__main__":
    main()