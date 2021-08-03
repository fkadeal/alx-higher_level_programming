#!/usr/bin/node
const _argv = process.argv;
if (typeof _argv[2] === 'undefined') {
  console.log('No argument');
} else {
  console.log(_argv[2]);
}
