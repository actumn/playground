import { onDestroy } from 'svelte';

export function onInterval(callback, milliseconds) {
	// implementation goes here
	const interval = setInterval(callback, milliseconds);
	
	onDestroy(() => {
		clearInterval(interval);
	})
}