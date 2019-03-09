import React, { Component } from 'react';
import ReactDOM from 'react-dom';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import OutlinedInput from '@material-ui/core/OutlinedInput';
import InputLabel from '@material-ui/core/InputLabel';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import Select from '@material-ui/core/Select';
import { DONE } from './SelectConstants';

const styles = theme => ({
  root: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  formControl: {
    margin: theme.spacing.unit,
    minWidth: 180,
  },
  selectEmpty: {
    marginTop: theme.spacing.unit * 2,
  },
});

class SelectComponent extends Component {
  static propTypes = {
    data: PropTypes.array.isRequired,
    disabled: PropTypes.bool,
    handleChange: PropTypes.func.isRequired,
    status: PropTypes.string.isRequired
  }

  state = {
    selectedValue: '',
    labelWidth: 0,
  };

  componentDidMount() {
    this.setState({
      labelWidth: ReactDOM.findDOMNode(this.InputLabelRef).offsetWidth,
    });
  }

  handleChange = event => {
    const value = event.target.value;
    this.setState({ selectedValue: value });
    this.props.handleChange(value);
  };

  renderMenuItems = (items) => {
    return items.map(this.renderMenuItem);
  }

  renderMenuItem(item, index) {
    const { id, name } = item;
    return <MenuItem key={id} value={item}>{name}</MenuItem>;
  }

  render() {
    const { selectedValue } = this.state;
    const { data, classes, label, status, disabled } = this.props;

    return (
      <form className={classes.root} autoComplete='off'>
        <FormControl
          variant='outlined'
          className={classes.formControl}
          disabled={status !== DONE || disabled }
          >
          <InputLabel ref={ref => { this.InputLabelRef = ref; }} >
            {label}
          </InputLabel>
          <Select
            value={selectedValue}
            onChange={this.handleChange}
            input={
              <OutlinedInput
                labelWidth={this.state.labelWidth}
                name={label}
                id={`${label}-input`}
              />
            }
          >
            {this.renderMenuItems(data)}
          </Select>
        </FormControl>
      </form>
    );
  }
}

export default withStyles(styles)(SelectComponent);
