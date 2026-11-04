# Using an API

* Interact with an API so that you can bring data into your web application.

---

[Fetch example](../webdev/15_resource_fetch.html)

## Predict & Run

1. Open this code in your editor.
1. What will this code do?
*Your answer here.*
1. Open the code in your browser.
1. Test it, and describe your tests.
*Your answer here.*
1. Was your prediction correct?
*Your answer here.*

---

[Fetch example](../webdev/15_resource_fetch.html)

## Inspect

The code features three new tools.
* `fetch`
* `await`
* `async`

1. Research what each of these does.
*Your answer here, then check it with your neighbour.*
1. How long might a web request take?
(think of times you've waited for a swirling page load)
*Your answer here.*
1. What would happen if you paused all interaction while waiting for a web request to finish?
*Your answer here.*

---

## Debug

1. What happens if you change the URL to a non-existent resource?
	* *Describe what you see in the browser.*
	* *Describe what you see in the console.*
	* *Describe what you see in the network tab.*
1. What happens if you remove the `await` keyword?
	* *Describe what you see in the browser.*
	* *Describe what you see in the console.*
	* *Describe what you see in the network tab.*
1. What happens if you remove the `async` keyword?
	* *Describe what you see in the browser.*
	* *Describe what you see in the console.*
	* *Describe what you see in the network tab.*

---

## Debug

The process that I call "fish bowl" is a way of testing code in a controlled environment.
My code samples in the course have been examples of "fish bowl" code.
They are in a simple environment, with no other code to interfere with the test.
I can then test the code in isolation, before putting it into the larger project.

If my first attempt at an piece of code doesn't work, I will usually put it in as simple an environment as possible, a "fish bowl".

---

## Adapt

1. Add and update a `loading` variable while the `fetch` is in progress.
1. Tweak the website so it displays some indicator that the request is in progress.

---

## Make

Find an API relevant to your project.
Integrate it into your project, and demonstrate that it works.

---

## Evaluate

* What resources are available via an API?
*Your answers here, we'll see how many times we can go around the room.*
