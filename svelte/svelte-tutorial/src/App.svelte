<script>
	import CountButton from './CountButton.svelte';
	import ExportExample from './ExportExample.svelte'
	import Info from './Info.svelte'
	import Logic from './Logic.svelte'
	import EachBlock from './EachBlock.svelte'
	import AsyncBlock from './AsyncBlock.svelte'
	import OnMousemove from './OnMousemove.svelte'
	import Inner from './Inner.svelte'
	import Outer from './Outer.svelte'
	import FancyButton from './FancyButton.svelte'
	import BindingInput from './BindingInput.svelte'
	import BindingInput2 from './BindingInput2.svelte'
	import BindComponent from './BindComponent.svelte'

	const name = 'world';
	const pkg = {
		name: 'svelte',
		version: 3,
		speed: 'blazing',
		website: 'https://svelte.dev',
	}
</script>

<h1>Hello {name}!</h1>
<BindComponent></BindComponent>
<CountButton></CountButton>
<ExportExample answer={42}></ExportExample>
<ExportExample></ExportExample>
<Info {...pkg}></Info>
<Logic></Logic>
<EachBlock></EachBlock>
<AsyncBlock></AsyncBlock>
<Outer on:message={e => alert(e.detail.text)}></Outer>
<FancyButton on:click={() => alert('clicked')} />
<BindingInput></BindingInput>
<BindingInput2></BindingInput2>
<OnMousemove></OnMousemove>
