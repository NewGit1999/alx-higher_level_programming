#!/usr/bin/node
exports.converter = function (base) {
  return (conv) => conv.toString(base);
};
