NOTE: Although Atom has been sunset, I will be maintaining this theme. I plan to publish to [Pulsar](https://pulsar-edit.dev/)'s (a community-driven effort to continue Atom) [package repository](https://web.pulsar-edit.dev/)

# fall-syntax
![Color Contrast Check](https://github.com/ThatXliner/fall-syntax/workflows/Color%20Contrast%20Check/badge.svg) [![APM](https://img.shields.io/apm/dm/fall-syntax)](https://atom.io/themes/fall-syntax) [![APM](https://img.shields.io/apm/l/fall-syntax)](https://atom.io/themes/fall-syntax) [![Built with Atom](https://img.shields.io/badge/Built%20with-Atom-brightgreen?logo=atom)](https://atom.io/)

![Banner](https://raw.githubusercontent.com/ThatXliner/fall-syntax/master/banner.png)

*Fall Syntax* is a syntax theme with 3 design points in mind:

 - Reduce [blue light](https://www.verywellhealth.com/blue-light-exposure-3421985)\*
 - Make code clear
 - Still look good

<sub>*Not clinically proven. Coding breaks are still recommended.</sub>

---

![A screenshot of the syntax theme](./screenshot.png)

---


I've sought out to build a syntax theme on top of those principals; something that minimizes the blue but still looks good. Why? I knew that [blue light causes eyestrain and headaches](https://www.foreyes.com/blog/10-ways-how-blue-light-can-affect-you), which are a nuisance for the programmer (and the average computer user).

After about a month of color-picking, discussion, and color-tweaking, *Fall Syntax* was here. Every hue, every shade, was **meticulously hand-picked**, tested, and **checked against standards** such as the [WCAG 2.0 contrast ratio criterion](https://www.w3.org/TR/UNDERSTANDING-WCAG20/visual-audio-contrast-contrast.html).

Naturally, the colors are reddish and aesthetic, giving that **post-summer vibe**.

Besides warm colors, *Fall Syntax* features some nice **perks** such as

 - Trivial components of code (like comments and bracket pairs) are **faded**
 - Consistent color semantics across languages (e.g. you will find definitions of classes or functions as a green keyword followed by a purple name)
 - **Increased contrast** on function/class definitions\*

Enjoy!

<sub>*support may vary depending on language. Check the FAQ for more info.</sub>

---

This is my first syntax theme 🎉, originally forked from [Atomic-monokai-pro-syntax][1]. Except now, this looks *nothing* like [atomic-monokai-pro-syntax][1].

I hope you like it! ❤️. If you do, **please star this repo and star this theme on Atom**. That way, you can let other people find this theme.

Hey, if you don't like this syntax theme ("it's too reddish!") I *highly recommend* @tterb's [Atomic-monokai-pro-syntax][1] or @jackw01's [summer-night-syntax](https://atom.io/themes/summer-night-syntax). @KomodoKode's personal favorite (how dare he not use Fall Syntax) is Atom's built-in One Dark. [Nord](https://www.nordtheme.com/) is pretty good, too.

## Installation

This theme can be installed from within Atom or via the command:
```sh
$ apm install fall-syntax
```
After installation, you can activated by going to the **Settings > Themes** section and selecting it from the **Syntax Themes** drop-down menu.

## Color palette

| Color        | Preview                                        | Hex       |
|--------------|------------------------------------------------|-----------|
| Pink         | ![](https://readme-swatches.vercel.app/FF7092) | `#FF7092` |
| Orange       | ![](https://readme-swatches.vercel.app/F99270) | `#F99270` |
| Light Orange | ![](https://readme-swatches.vercel.app/FFB370) | `#FFB370` |
| Peach        | ![](https://readme-swatches.vercel.app/F9C19A) | `#F9C19A` |
| Green        | ![](https://readme-swatches.vercel.app/7EC892) | `#7EC892` |
| Purple       | ![](https://readme-swatches.vercel.app/D6ABEE) | `#D6ABEE` |
| Maroon       | ![](https://readme-swatches.vercel.app/C65882) | `#C65882` |
| Foreground   | ![](https://readme-swatches.vercel.app/E3DEDF) | `#E3DEDF` |
| Punctuation  | ![](https://readme-swatches.vercel.app/A29094) | `#A29094` |
| Background   | ![](https://readme-swatches.vercel.app/262022) | `#262022` |


## FAQ

Q: **I need this for other editors**

A: Current ports:

 - [Fall Syntax for VSCode](https://github.com/ThatXliner/fall-syntax-vscode) (Unfinished)
 - [Fall Syntax for Sublime text](https://github.com/imnotril/fall-syntax-sublime-text) (note: this is a 3rd-party contribution)

If you have made a port, please send a pull request updating this list.

Q: **This syntax highlighting is degraded**

A: You're probably having tree-sisters parsing on. While it is a promising technology, it currently seems to degrade syntax highlighting. I recommend you turn it off on Settings > Core. If that's not the case **feel free to complain in the issues or send a pull request!**. I have rewritten the \_base.less by hand so I have probably dropped support for some markup/programming languages.

Q: **This looks like (insert some theme name)**

A: Welp. Great minds think alike!

Q: **How can I contribute?**

A: Either ~~complain about the colors~~ professionally critique the theme in the issues or send a pull request for some different colors/arrangements. Or you can **help me port this theme to other editors** I'll merge it if I like it!

<!-- ## More images

<details>

<summary>Click to expand</summary>

<img src="./screenshot1.png"></img>
<img src="./screenshot2.png"></img>
</details> -->

## Credits

Credits to

 - My ***epic*** friends [@KomodoKode](https://github.com/KomodoKode) and [@thatdevboyjun](https://github.com/thatdevboyjun) for feedback, suggestions, and critique! Thanks guys!
 - @tterb for his *amazing* https://github.com/tterb/Atomic-Monokai-Pro-syntax
 - The [City lights theme][2] for major inspiration
 - Wimer Hazenberg and his [Monokai Pro theme](https://monokai.pro/), which has heavily influenced the design. You can still see traces of Monokai hidden in the theme
 - [Coolors.co](https://coolors.co/) for the *epic* palette generator (and color editor)

[1]: https://github.com/tterb/Atomic-Monokai-Pro-syntax
[2]: http://citylights.xyz/
[tool]: https://mswift42.github.io/themecreator/
