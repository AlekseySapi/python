import os
from pydub import AudioSegment
from mutagen.flac import FLAC, Picture
from mutagen.oggvorbis import OggVorbis
from mutagen.ogg import OggPage
from mutagen.mp3 import EasyMP3
from mutagen.mp4 import MP4, MP4Cover
from mutagen.wavpack import WavPack
from mutagen.id3 import ID3, APIC

line = '\n################# ################# #################'

def extract_metadata(input_file):
    """ Извлекает метаданные и обложку из исходного файла """
    ext = os.path.splitext(input_file)[1].lower()
    metadata = {}
    cover = None

    try:
        if ext == ".flac":
            audio = FLAC(input_file)
            metadata = {k: v for k, v in audio.items()}
            if audio.pictures:
                cover = audio.pictures[0]  # Берём первую обложку

        elif ext == ".ogg":
            audio = OggVorbis(input_file)
            metadata = {k: v for k, v in audio.items()}
            try:
                ogg_file = OggPage(input_file)
                for page in ogg_file:
                    if page.header_type & 2:
                        cover = page.data
                        break
            except Exception:
                pass

        elif ext == ".mp3":
            audio = EasyMP3(input_file)
            metadata = {k: v for k, v in audio.items()}
            id3 = ID3(input_file)
            for tag in id3.values():
                if isinstance(tag, APIC):  # APIC – это обложка
                    cover = tag.data
                    break

        elif ext == ".m4a":     # Не работает корректно, если пойму проблему - надо исправить потом
            audio = MP4(input_file)
            metadata = {k: [str(v) for v in v] if isinstance(v, list) else [str(v)] for k, v in audio.items()}
            if "covr" in audio:
                cover_data = audio["covr"][0]
                cover = bytes(cover_data) if isinstance(cover_data, MP4Cover) else cover_data

        elif ext == ".wav":
            audio = WavPack(input_file)
            metadata = {k: v for k, v in audio.items()}

    except Exception as e:
        print(f"⚠️   Ошибка при извлечении метаданных.")

    return metadata, cover

def apply_metadata(output_file, metadata, cover):
    """ Записывает метаданные и обложку в FLAC-файл """
    try:
        audio = FLAC(output_file)
        audio.clear()  # Удаляем старые теги, чтобы не было дубликатов

        for key, value in metadata.items():
            audio[key] = value

        if cover:
            pic = Picture()
            if isinstance(cover, Picture):
                pic = cover
            else:
                pic.type = 3  # Front Cover
                pic.mime = "image/jpeg" if cover[:3] == b"\xff\xd8\xff" else "image/png"
                pic.data = cover
            audio.add_picture(pic)

        audio.save()
    except Exception as e:
        print(f"⚠️   Ошибка при сохранении метаданных.")

def compress_flac(input_file, output_file):
    """ Конвертирует аудиофайл в FLAC с сохранением метаданных """
    metadata, cover = extract_metadata(input_file)

    audio = AudioSegment.from_file(input_file)
    audio.export(output_file, format="flac", parameters=["-compression_level", "8"])

    apply_metadata(output_file, metadata, cover)

def main():
    print(line)
    print("     < Сжатие аудиоформата FLAC (без потерь) >\n       MP3, OGG, WAV переводятся в FLAC\n")
    while True:
        print(line)
        file = input("# Введите имя файла:\n> ")
        if not os.path.isfile(file):
            print("\n  Файл не найден.\n")
            continue

        filename, ext = os.path.splitext(file)
        if ext.lower() not in ('.flac', '.ogg', '.mp3', '.wav'):
            print("\n\n⚠️  Ошибка: Неверный формат файла.\n")
            continue
        output_file = f"{filename}_opt.flac"
        
        compress_flac(file, output_file)
        
        print(f"\n\n✅  Файл оптимизирован и сохранён!\n")

if __name__ == "__main__":
    main()