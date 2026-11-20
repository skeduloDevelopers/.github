# .github
## Card images

Each card in `profile/README.md` has a 1920×1080 image in `profile/images/`: a screenshot set down and to the right on the blue gradient, running off the right and bottom edges, with a rounded top-left corner.

To make one from a browser screenshot (needs Python 3 and [Pillow](https://pypi.org/project/pillow/)):

```bash
python3 profile/images/make-card.py screenshot.png profile/images/MyExamples.png
```

The screenshot is enlarged 1.35 times by default, which suits a 1440×900 capture. Pass a different scale as a third argument to show more or less of it. The script stops if the enlarged screenshot would not fill the frame.
