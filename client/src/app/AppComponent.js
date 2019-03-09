import React, { Component } from 'react';
import PropTypes from 'prop-types';
import styles from './App.css';
import SelectComponent from '../select/SelectContainer';
import Dialog from '../dialog/DialogComponent';

export default class AppComponent extends Component {
  static propTypes = {
    diagnoses: PropTypes.array,
    isDialogOpen: PropTypes.bool.isRequired,
    handleCloseDialog: PropTypes.func.isRequired,
    handleCloseDialogConfirm: PropTypes.func.isRequired,
    handleSelectChange: PropTypes.func.isRequired,
    status: PropTypes.string,
    selectedSymptom: PropTypes.object,
  };

  state = {
    topDiagnosis: {}
  };

  componentWillReceiveProps(nextProps) {
    const { diagnoses } = nextProps;
    if (diagnoses.length > 0) {
      this.setState({ topDiagnosis: diagnoses[0] });
    }
  }

  handleCloseDialogConfirm = () => {
    const { topDiagnosis } = this.state;
    const { handleCloseDialogConfirm } = this.props;
    handleCloseDialogConfirm(topDiagnosis);
  }

  render() {
    const { topDiagnosis } = this.state;
    const {
      handleCloseDialog,
      handleSelectChange,
      isDialogOpen,
      selectedSymptom,
    } = this.props;

    return (
      <div className={styles.app}>
        <SelectComponent
          label={"Sympom Selector"}
          handleChange={handleSelectChange}
          disabled={!!selectedSymptom.id}
        />
        <Dialog
          confirmText="Yes"
          denyText="No"
          description={`Sounds like you might have ${topDiagnosis.name}`}
          handleClose={handleCloseDialog}
          handleCloseConfirm={this.handleCloseDialogConfirm}
          handleCloseDeny={handleCloseDialog}
          isOpen={isDialogOpen}
          title={`You picked ${selectedSymptom.name}`}
        />
      </div>
    );
  }
}
