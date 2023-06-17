#!/usr/bin/node
exports.esrever = function (list) {
  const revversion = [];
  for (let i = list.length - 1; i >= 0; i--) {
    revversion.push(list[i]);
  }
  return revversion;
};
