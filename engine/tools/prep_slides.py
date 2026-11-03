"""Prepare a lecture's slides.

  python engine/tools/prep_slides.py text  5 source/Lecture_5.pdf        -> source/L5.txt (pdftotext -layout)
  python engine/tools/prep_slides.py sheet 5 source/Lecture_5.pdf        -> build/contact_L5.jpg (numbered thumbnails to pick figure slides)
  python engine/tools/prep_slides.py figs  5 source/Lecture_5.pdf 4 8 12 -> slides/L5-4.jpg, L5-8.jpg ... (only slides with real figures)

Paths are relative to the course folder (COURSE=courses/<name>). For PPTX, convert first:
  soffice --headless --convert-to pdf deck.pptx
"""
import os, sys, subprocess, tempfile, glob
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from common import COURSE, BUILD, SLIDES
from PIL import Image, ImageChops, ImageDraw


def trim(im):
    bg = Image.new(im.mode, im.size, im.getpixel((0, 0)))
    box = ImageChops.difference(im, bg).getbbox()
    return im.crop(box) if box else im


def render(pdf, first, last, dpi):
    d = tempfile.mkdtemp()
    subprocess.run(['pdftoppm', '-r', str(dpi), '-f', str(first), '-l', str(last), '-jpeg', str(pdf), f'{d}/p'], check=True)
    return sorted(glob.glob(f'{d}/p-*.jpg'), key=lambda f: int(f.rsplit('-', 1)[1].split('.')[0]))


def main():
    mode, lec, pdf = sys.argv[1], sys.argv[2], COURSE / sys.argv[3]
    if mode == 'text':
        (COURSE / 'source').mkdir(exist_ok=True)
        out = COURSE / 'source' / f'L{lec}.txt'
        subprocess.run(['pdftotext', '-layout', str(pdf), str(out)], check=True)
        print(out)
    elif mode == 'sheet':
        info = subprocess.run(['pdfinfo', str(pdf)], capture_output=True, text=True).stdout
        n = int(info.split('Pages:')[1].split()[0])
        files = render(pdf, 1, n, 30)
        tw, th, cols = 320, 240, 6
        sheet = Image.new('RGB', (cols * tw, ((len(files) + cols - 1) // cols) * th), 'white')
        dr = ImageDraw.Draw(sheet)
        for i, f in enumerate(files):
            im = Image.open(f); im.thumbnail((tw - 10, th - 30))
            x, y = (i % cols) * tw, (i // cols) * th
            sheet.paste(im, (x + 5, y + 25)); dr.text((x + 8, y + 5), f'p{i + 1}', fill='red')
        out = BUILD / f'contact_L{lec}.jpg'
        sheet.save(out, quality=80)
        print(out)
    elif mode == 'figs':
        SLIDES.mkdir(exist_ok=True)
        for p in sys.argv[4:]:
            f = render(pdf, p, p, 130)[0]
            im = trim(Image.open(f).convert('RGB'))
            if im.width > 1100:
                im = im.resize((1100, round(im.height * 1100 / im.width)))
            out = SLIDES / f'L{lec}-{p}.jpg'
            im.save(out, quality=72, optimize=True)
            print(out)
    else:
        print(__doc__)


if __name__ == '__main__':
    main() if len(sys.argv) >= 4 else print(__doc__)
