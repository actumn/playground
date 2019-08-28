// try clone: updateDelayTimer, processJob, processJobs
// https://github.com/OptimalBits/bull/blob/develop/lib/queue.js

// eslint-disable-next-line no-unused-vars
let delayTimer;

function processJob() {
  console.log('processJob');
  return Promise.resolve();
}

function processJobOnNextTick(processJobsFunc) {
  console.log('processJobOnNextTick')
  return processJob()
    // eslint-disable-next-line no-use-before-define
    .then(processJobsFunc);
}

function processJobs(resolve) {
  const processJobsFunc = processJobs.bind(resolve);
  console.log('processjobs');
  process.nextTick(() => {
    processJobOnNextTick(processJobsFunc);
  });
}

function run() {
  const promises = [];

  return new Promise(() => {
    promises.push(
      // eslint-disable-next-line no-use-before-define
      new Promise(resolve => processJobs(resolve)),
    );

    return Promise.all(promises);
  });
}

function timer() {
  return new Promise(resolve => resolve())
    .then(() => {
      console.log('timerPromise');
      if (delayTimer) {
        clearTimeout(delayTimer);
      }

      const delay = 5000;
      delayTimer = setTimeout(() => timer(), delay);

      return null;
    }).catch(err => console.error(err));
}

function init() {
  return new Promise(resolve => resolve())
    .then(timer);
}

function start() {
  console.log('start');
  return run();
}

function timerProcess() {
  return init().then(() => start());
}

timerProcess();

