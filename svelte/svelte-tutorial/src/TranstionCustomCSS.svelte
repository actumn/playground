<script>
	import { elasticOut } from 'svelte/easing';
	
	function fade(node, {
		delay = 0,
		duration = 400
	}) {
		const o = +getComputedStyle(node).opacity;
		
		return {
			delay,
			duration,
			css: t => `opacity: ${t * o}`
		}
	}
	
	let visible = true;

	function spin(node, { duration }) {
		return {
			duration,
			css: t => {
				const eased = elasticOut(t);
				
				return `
transform: scale(${eased}) rotate(${eased * 1080}deg);
color: hsl(
	${~~(t * 360)},
	${Math.min(100, 1000 - 1000 * t)}%,
	${Math.min(50, 500 - 5000 *t)}%
);`
			}
		};
	}
</script>

<style>
	.centered {
		position: absolute;
		left: 50%;
		top: 50%;
		transform: translate(-50%,-50%);
	}

	span {
		position: absolute;
		transform: translate(-50%,-50%);
		font-size: 4em;
	}
</style>

<label>
	<input type="checkbox" bind:checked={visible}>
	visible
</label>

{#if visible}
	<div class="centered" in:spin="{{duration: 8000}}" out:fade>
		<span>transitions!</span>
	</div>
{/if}