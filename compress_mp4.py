import os
import subprocess

line = '\n################# ################# #################'

def get_video_info(file):
    """Получает информацию о файле: кодек видео, кодек аудио, размер файла."""
    cmd = f'ffprobe -v error -select_streams v:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "{file}"'
    video_codec = subprocess.check_output(cmd, shell=True).decode().strip()
    
    cmd = f'ffprobe -v error -select_streams a:0 -show_entries stream=codec_name -of default=noprint_wrappers=1:nokey=1 "{file}"'
    try:
        audio_codec = subprocess.check_output(cmd, shell=True).decode().strip()
    except subprocess.CalledProcessError:
        audio_codec = "unknown"
    
    file_size = os.path.getsize(file)
    return video_codec, audio_codec, file_size


def convert_video(input_file, output_file, codec, crf, preset, needs_audio_convert):
    """Конвертирует видео с нужными параметрами."""
    audio_settings = "-c:a aac -b:a 128k" if needs_audio_convert else "-c:a copy"

    cmd = f'ffmpeg -i "{input_file}" -c:v {codec} -crf {crf} -preset {preset} {audio_settings} "{output_file}"'
    subprocess.run(cmd, shell=True, check=True)


def main():
    print(line)
    print("    < Конвертер/оптимизатор из WebM/MP4 в MP4 >")
    
    while True:
        print(line)
        file = input("# Введите имя файла (MP4/WebM):\n> ")
        if not os.path.isfile(file):
            print("Файл не найден.\n")
            continue
        
        filename, ext = os.path.splitext(file)
        if ext.lower() not in ('.mp4', '.webm'):
            print("\n⚠️  Ошибка: Поддерживаются только MP4 и WebM.\n")
            continue

        print("\n# Выбор кодека:\n  1 - H.265 (HEVC)\n  2 - AV1")
        codec_choice = ''
        while codec_choice not in ('1', '2'):
            codec_choice = input("> ")
        codec = "libx265" if codec_choice == '1' else "libaom-av1"

        if codec_choice == '1':
            print("\n# Выберите качество (CRF):\n  1 - Высокое (18)\n  2 - Выше среднего (24)\n  3 - Среднее (28)\n  4 - Максимальное сжатие (32)")
            crf_choice = ''
            while crf_choice not in ('1', '2', '3', '4'):
                crf_choice = input("> ")
            crf = {'1': 18, '2': 24, '3': 28, '4': 32}[crf_choice]
        else:
            print("\n# Выберите качество (CRF):\n  1 - Высокое (24)\n  2 - Среднее (30)\n  3 - Максимальное сжатие (34)")
            crf_choice = ''
            while crf_choice not in ('1', '2', '3'):
                crf_choice = input("> ")
            crf = {'1': 24, '2': 30, '3': 34}[crf_choice]

        print("\n# Выберите скорость кодирования (Preset):\n  1 - medium\n  2 - slow\n  3 - slower\n  4 - veryslow")
        preset_choice = ''
        while preset_choice not in ('1', '2', '3', '4'):
            preset_choice = input("> ")
        preset = { '1': 'medium', '2': 'slow', '3': 'slower', '4': 'veryslow' }[preset_choice]

        video_codec, audio_codec, original_size = get_video_info(file)
        needs_audio_convert = audio_codec == "opus"

        output_file = f"{filename}_opti.mp4"
        print(f"\n\n⏳ Начинаем конвертацию {file} → {output_file}\n Кодек: {codec} | CRF: {crf} | Preset: {preset}\n\n")
        convert_video(file, output_file, codec, crf, preset, needs_audio_convert)

        new_size = os.path.getsize(output_file)
        reduction = 100 - (new_size / original_size * 100)
        print(line)
        print(f"\n\n✅ Готово! Размер уменьшился на {reduction:.2f}% ({original_size/1e6:.2f}MB → {new_size/1e6:.2f}MB)\n")
        break


if __name__ == "__main__":
    main()