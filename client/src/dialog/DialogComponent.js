import React, { Component } from 'react';
import PropTypes from 'prop-types';
import Button from '@material-ui/core/Button';
import Dialog from '@material-ui/core/Dialog';
import DialogActions from '@material-ui/core/DialogActions';
import DialogContent from '@material-ui/core/DialogContent';
import DialogContentText from '@material-ui/core/DialogContentText';
import DialogTitle from '@material-ui/core/DialogTitle';

export default class DialogComponent extends Component {

  static propTypes = {
    confirmText: PropTypes.string.isRequired,
    denyText: PropTypes.string.isRequired,
    description: PropTypes.string.isRequired,
    handleClose: PropTypes.func.isRequired,
    handleCloseConfirm: PropTypes.func.isRequired,
    handleCloseDeny: PropTypes.func.isRequired,
    isOpen: PropTypes.bool.isRequired,
  };

  render() {
    const {
      confirmText,
      denyText,
      description,
      handleClose,
      handleCloseConfirm,
      handleCloseDeny,
      isOpen,
      title
    } = this.props;

    return (
      <div>
        <Dialog
          open={isOpen}
          onClose={handleClose}
        >
          <DialogTitle id="draggable-dialog-title">{title}</DialogTitle>
          <DialogContent>
            <DialogContentText>
              {description}
            </DialogContentText>
          </DialogContent>
          <DialogActions>
            <Button onClick={handleCloseDeny} color="primary">
              {denyText}
            </Button>
            <Button onClick={handleCloseConfirm} color="primary">
              {confirmText}
            </Button>
          </DialogActions>
        </Dialog>
      </div>
    );
  }
}
