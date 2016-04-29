import { renderComponent, expect } from '../test_helper';
import DropDown from '../../src/components/drop_down';

describe('DropDown', () => {
  let component;

  beforeEach(() => {
    component = renderComponent(DropDown);
  });

  it('has the class drop-down', () => {
    expect(component).to.have.class('drop-down');
  });

  it('has a drop-down menu', () => {
    expect(component.find('select')).to.exist;
  });
  
});
