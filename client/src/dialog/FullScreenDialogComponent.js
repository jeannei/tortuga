import React, { Component } from 'react';
import PropTypes from 'prop-types';
import { withStyles } from '@material-ui/core/styles';
import Dialog from '@material-ui/core/Dialog';
import ListItemText from '@material-ui/core/ListItemText';
import ListItem from '@material-ui/core/ListItem';
import List from '@material-ui/core/List';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Slide from '@material-ui/core/Slide';

const styles = {
  appBar: {
    position: 'relative',
  },
  flex: {
    flex: 1,
  },
};

function Transition(props) {
  return <Slide direction="up" {...props} />;
}

class FullScreenDialog extends Component {

  static propTypes = {
    data: PropTypes.array.isRequired,
    classes: PropTypes.object.isRequired,
    handleClick: PropTypes.func.isRequired,
    isOpen: PropTypes.bool.isRequired,
    title: PropTypes.string
  };

  handleClick = (item) => {
    const { handleClick } = this.props;
    handleClick(item);
  }

  renderListItem = (item, index) => {
    const { id, name } = item;
    return (
      <ListItem key={index} button onClick={this.handleClick.bind(null, item)}>
        <ListItemText key={id} primary={name} />
      </ListItem>
    );
  }

  render() {
    const { data, classes, isOpen, title } = this.props;
    return (
      <div>
        <Dialog
          fullScreen
          open={isOpen}
          onClose={this.handleClose}
          TransitionComponent={Transition}
        >
          <AppBar className={classes.appBar}>
            <Toolbar>
              <Typography variant="h6" color="inherit" className={classes.flex}>
                {title}
              </Typography>
            </Toolbar>
          </AppBar>
          <List>
            {data.map(this.renderListItem)}
          </List>
        </Dialog>
      </div>
    );
  }
}

export default withStyles(styles)(FullScreenDialog);
