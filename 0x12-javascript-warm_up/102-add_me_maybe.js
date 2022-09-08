#!/usr/bin/node
exports.addMeMaybe = (x, callback) => {
  callback(++x);
};
