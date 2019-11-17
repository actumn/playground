<script>
	let promise = getRandomNumber();

	async function getRandomNumber() {
		const res = await fetch(`https://svelte.dev/tutorial/random-number`);
		const text = await res.text();

		if (res.ok) {
			return text;
		} else {
			throw new Error(text);
		}
	}

	function handleClick() {
		promise = getRandomNumber();
	}
</script>

<button on:click={handleClick}>
	generate random number
</button>

<!-- replace this element -->
{#await promise}
  <p>...waiting</p>
{:then value}
	<p>
		The number is {value}
	</p>
{/await}