import React from 'react';
import renderer from 'react-test-renderer';

import App from '../containers/App';


it('App renders correctly', () => {
  const tree = renderer.create(
    <App />
  ).toJSON();
  expect(tree).toMatchSnapshot();
});
