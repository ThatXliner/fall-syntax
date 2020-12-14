# fall-syntax
![APM](https://img.shields.io/apm/dm/fall-syntax) ![APM](https://img.shields.io/apm/l/fall-syntax) ![Build with Atom](https://img.shields.io/badge/Built%20with-Atom-brightgreen?logo=atom)

*Fall Syntax* is a syntax theme with 3 points in mind:

 - Dark, reducing overall energy consumption
 - Warm colors like red (but not too red), to reduce [blue light](https://www.verywellhealth.com/blue-light-exposure-3421985)
 - Meticulously conditioned color so it still looks good.

---

![A screenshot of the syntax theme](./screenshot.png)

---

Unlike most other themes, this theme aims to **reduce eye strain** using **warmer colors**. This works by minimizing the amount of blue light (which can harm your eyes) shown on the screen. You can call it the opposite of [City Lights][2] :wink:.

It's also designed to help the programmer **focus**, *greying out comments* and increasing contrast on **function/class definitions**. `TODO`s and strings still get some limelight, though.

Being a **dark theme** (which *looks great* during the day *or* night), it helps **reduce energy consumption**. While this **may not be** a huge problem, I've been lately **clutching my battery** with my *Intel-powered Mac* :grimacing:.

---

This is my first syntax theme, based off of (and originally forked from) [Atomic-monokai-pro-syntax][1]. Except now, this looks *nothing* like [atomic-monokai-pro-syntax][1].

I hope you like it! :heart:

## Installation

This theme can be installed from within Atom or via the command:
```sh
$ apm install fall-syntax
```
After installation, you can activated by going to the **Settings > Themes** section and selecting it from the **Syntax Themes** drop-down menu.

## Creation and design

I took three different ways until deciding on how to make this theme

### Just make it redder

I loved [the monokai pro syntax theme][1] for [Atom](https://atom.io/). But just warming the colors isn't creative and **the result was ugly**.

So I chose a different way.

### Monochromatic red!

Yeah, um, there's not going to be space for contrast. *Fall Syntax* uses contrast to help with visual grepping for definitions.

### Get a reddy palette and edit that

So I used [Coolors.co](https://coolors.co/) to help me generate some colors. I selected the ones I like and kept on spamming <kbd>space</kbd> until I liked the palette.

Then I filled in the Less and kept on fine-tune and tweaked the colors until I liked them. **This is the method I settled with.**

**NOTE**: plainly choosing the colors from a photo and smacking it here may seem nice but actually, it's not going to be well calibrated. The colors here are *meticulously* chosen with great care.

## FAQ

**Hey, did you steal some monokai colors!?**

A: No, great minds think alike

## Credits

Credits to

 - @tterb for his *amazing* https://github.com/tterb/Atomic-Monokai-Pro-syntax
 - The [City lights theme][2] for major inspiration
 - Wimer Hazenberg and his [Monokai Pro theme](https://monokai.pro/), which has heavily influenced the design. You can see traces of Monokai hidden in the theme
 - [Coolors.co](https://coolors.co/) for the *epic* palette generator (and color editor)

[1]: https://github.com/tterb/Atomic-Monokai-Pro-syntax
[2]: http://citylights.xyz/
