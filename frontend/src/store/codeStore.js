import { writable } from 'svelte/store';

export const code = writable(`console.log('Hello world!');`);