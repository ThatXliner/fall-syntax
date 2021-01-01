# fall-syntax
[![APM](https://img.shields.io/apm/dm/fall-syntax)](https://atom.io/themes/fall-syntax) [![APM](https://img.shields.io/apm/l/fall-syntax)](https://atom.io/themes/fall-syntax) [![Build with Atom](https://img.shields.io/badge/Built%20with-Atom-brightgreen?logo=atom)](https://atom.io/)

> A syntax theme for your eyes

*Fall Syntax* is a syntax theme with 3 points in mind:

 - Reduce [blue light](https://www.verywellhealth.com/blue-light-exposure-3421985) by utilizing **warm colors**\*
 - Help you **focus** on code you need to focus on
 - Eye pleasing, with colors syncing in **harmony**

<sub>*does not prevent 100% blue light from monitor. DO NOT USE AS A REPLACEMENT FOR BLUE LIGHT BLOCKING GLASSES. Coding breaks are still recommended.</sub>

---

[![A screenshot of the syntax theme](https://raw.githubusercontent.com/ThatXliner/fall-syntax/master/screenshot.png)](https://github.com/ThatXliner/fall-syntax/blob/master/screenshot.png)

*Font used in screenshot: [Fira Code](https://github.com/tonsky/FiraCode) with ligatures `ss01`, `ss02`, `ss03`, `ss05`, and `ss06` enabled*

---

Unlike most other themes, this theme aims to **reduce eye strain** using **warmer colors**. This works by *minimizing* the amount of blue light (which can harm your eyes) shown on the screen. You can call it the opposite of [City Lights][2] 😉.

It's also designed to help the programmer **focus**, *greying out comments* and increasing contrast on **function/class definitions**\*, helping with visual grepping by providing anchor points of contrast 👀.

And here's some personal preference: it's a **dark theme** which *looks great*\*\* during the day *or* night (light version of theme is work in progress). Thus helping you **reduce overall energy consumption**. While this **may not be** a huge problem, I've been lately **clutching my battery** with my *Intel-powered Mac* 😬.

<sub>*support may vary depending on language</sub>

<sub>**purely (biased) opinion</sub>

---

This is my first syntax theme 🎉, based off of (and originally forked from) [Atomic-monokai-pro-syntax][1]. Except now, this looks *nothing* like [atomic-monokai-pro-syntax][1].

I hope you like it! ❤️. If you do, **please star this repo and star this theme on Atom**. That way, *you* can let other people find this awesome theme. Who doesn't want that?

**Sidenote:** I've only well-tested this on python, *but* the other languages (whether it's in `tests/syntax/` or not) *should* have decent syntax highlighting (thanks to @tterb, again). If not, please open an issue!

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

Yeah, um, there's not going to be space for contrast.

### Get a reddy palette and edit that

So I used [Coolors.co](https://coolors.co/) to help me generate some colors. I selected the ones I like and kept on spamming <kbd>space</kbd> until I liked the palette.

Then I filled in the Less and kept on fine-tune and tweaked the colors until I liked them. **This is the method I settled with.**

**NOTE**: plainly choosing the colors from a photo and smacking it here may seem nice but actually, it's not going to be well calibrated. The colors here are *meticulously* chosen with great care.

## FAQ

Q : **Hey, did you steal some monokai colors!?**

A: No, great minds think alike

Q : **Why does it look so similar to monokai?**

A: I'm working on making it unique, but yeah: that's the influence. Unlike Monokai, the colors are more warm (and I try to reduce the amount of blue). You can help me make this syntax it's own!

Q : **How can I contribute?**

A: Either ~~complain about the colors~~ professionally critique the theme in the issues or send a pull request for some different colors/arrangements. I'll merge it if I like it! **Some languages may be poorly syntax highlighted.** If you use those languages, feel free to complain in the issues or send a pull request!

## Credits

Credits to

 - @tterb for his *amazing* https://github.com/tterb/Atomic-Monokai-Pro-syntax
 - The [City lights theme][2] for major inspiration
 - Wimer Hazenberg and his [Monokai Pro theme](https://monokai.pro/), which has heavily influenced the design. You can see traces of Monokai hidden in the theme
 - [Coolors.co](https://coolors.co/) for the *epic* palette generator (and color editor)

[1]: https://github.com/tterb/Atomic-Monokai-Pro-syntax
[2]: http://citylights.xyz/
