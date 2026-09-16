# Responsive Styling

* Accomodate user preferences in your styling so that your websites are more appealing

---

## Do Now

* Sketch the powerpoint layout using only T junctions and lines

---

## meta viewport

Turn off all the adaptions that smartphones put in place for small screens.
Various hacks were made to cope with websites that aren't designed for mobiles.
However, these cause problems for websites that are designed for the modern web.

```
<head>
  <meta
    name="viewport"
    content="width=device-width"
  />
</head>
```

---

## em & other units

The `em` is a unit of measurement from laying out print runs of newpapers.
It is the width of the letter m in that situation.
It's very useful once you get used to it.
We quite often want an element to be "a few words wide".

```css
div {
    padding: 2em;
}
```

1. Look up `%`, `vw` and `vh`.

---

## @media width

```css
@media (min-width: 799px) {
    navbar.burger {
        display: none;
    }
}
```

1. What do you think this will do?
1. Teacher to demonstrate selecting device emulation.
1. Students to experiment with min-width

---

## @media color-scheme

```css
@media (prefers-color-scheme: dark) {
    html {
        background: black;
    }
}
```

1. What do you think this will do?
1. Students to test this.

---

## CSS Variables

```css
html {
    --background: hsl(0, 0%, 100%);
    --main: hsl(0, 0%, 15%);
    --action: hsl(120, 100%, 15%);
}
```

Whenever you reference these within the html element, they are substituted in.

```css
html {
    background: var(--background);
    color: var(--main);
}
```
