<script>
	import { onMount } from 'svelte';
	
	let photos = [];
	
	onMount(async () => {
    // It's recommended to put the fetch in onMount rather than at the top level of the <script> 
    // because of server-side rendering (SSR).
    // ith the exception of onDestroy, lifecycle functions don't run during SSR, 
    // which means we can avoid fetching data that should be loaded lazily once the component has been mounted in the DOM.
		const res = await fetch(`https://jsonplaceholder.typicode.com/photos?_limit=20`);
		photos = await res.json();
	})
</script>

<style>
	.photos {
		width: 100%;
		display: grid;
		grid-template-columns: repeat(5, 1fr);
		grid-gap: 8px;
	}

	figure, img {
		width: 100%;
		margin: 0;
	}
</style>

<h1>Photo album</h1>

<div class="photos">
	{#each photos as photo}
		<figure>
			<img src={photo.thumbnailUrl} alt={photo.title}>
			<figcaption>{photo.title}</figcaption>
		</figure>
	{:else}
		<!-- this block renders when photos.length === 0 -->
		<p>loading...</p>
	{/each}
</div>