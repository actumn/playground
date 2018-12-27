// Import events module
var events = require('events');

// Create an eventEmitter object
var eventEmitter = new events.EventEmitter();

// Bind event and event handler as follows
eventEmitter.on('eventName', () => {
    console.log('eventName fired.')
});

// Fire an event
eventEmitter.emit('eventName');
