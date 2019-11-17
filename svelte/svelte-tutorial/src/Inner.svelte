<script>
	// setup code goes here
	import { createEventDispatcher } from 'svelte';

  // createEventDispatcher must be called when the component is first instantiated — 
  // you can't do it later inside e.g. a setTimeout callback. 
  // This links dispatch to the component instance.
	const dispatch = createEventDispatcher();

	function sayHello() {
		dispatch('message', {
			text: 'Hello!'
		});
	}
</script>

<button on:click={sayHello}>
	Click to say hello
</button>