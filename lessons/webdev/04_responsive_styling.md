# Responsive Styling

* Accomodate user preferences in your styling so that your websites are more appealing

---

## Do Now

* Sketch the powerpoint layout using only T junctions and lines

---

## meta viewport

Turn off all the adaptions that mobile phones try to put in place.

```
<head>
  <meta
    name="viewport"
    content="width=device-width"
  />
</head>
```

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

---

## em & other units

The `em` is a unit of measurement from laying out print runs of newpapers. It is the width of the letter `m` for that situation.

It's very useful once you get used to it, because we usually want to measure elements relative to the text.

```css
div {
    padding: 2em;
}
```

---

## @media width

```css
@media (min-width: 799px) {
    html {
        background: hotpink;
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

This is combines well with CSS variables to swap an entire palette out.
