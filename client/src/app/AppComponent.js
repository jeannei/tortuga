import React, { Component } from 'react';
import PropTypes from 'prop-types';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button'
import List from '@material-ui/core/List';
import ListItem from '@material-ui/core/ListItem';
import ListItemText from '@material-ui/core/ListItemText';
import styles from './App.css';
import SelectComponent from '../select/SelectContainer';
import DialogComponent from '../dialog/DialogComponent';
import FullScreenDialogCompnent from '../dialog/FullScreenDialogComponent';
import { DETERMINED, PENDING } from './AppConstants';

export default class AppComponent extends Component {
  static propTypes = {
    diagnoses: PropTypes.array,
    diagnosisStatus: PropTypes.string.isRequired,
    isDialogOpen: PropTypes.bool.isRequired,
    handleCloseDialog: PropTypes.func.isRequired,
    handleCloseDialogConfirm: PropTypes.func.isRequired,
    handleDiagnosisSlector: PropTypes.func.isRequired,
    handleRefresh: PropTypes.func.isRequired,
    handleSelectChange: PropTypes.func.isRequired,
    status: PropTypes.string,
    selectedDiagnosis: PropTypes.object,
    selectedSymptom: PropTypes.object,
  };

  handleCloseDialogConfirm = () => {
    const { handleCloseDialogConfirm, selectedDiagnosis } = this.props;
    handleCloseDialogConfirm(selectedDiagnosis);
  }

  renderDiagnosis = (totalFrequencies, item, index) => {
    const { selectedDiagnosis } = this.props;
    const text = `${item.name} - ${item.frequency / totalFrequencies * 100}%
    of people had a similar issue.`
    let style = {};

    if (item.id === selectedDiagnosis.id) {
      style = { backgroundColor: 'yellow' };
    }
    return (
      <ListItem key={index} style={style}>
        <ListItemText primary={text} />
      </ListItem>
    );
  }

  renderDialog() {
    const { handleCloseDialog, isDialogOpen, selectedSymptom, selectedDiagnosis } = this.props;
    return (
      <DialogComponent
        confirmText='Yes'
        denyText='No'
        description={`Sounds like you might have a ${selectedDiagnosis.name}.`}
        handleClose={handleCloseDialog}
        handleCloseConfirm={this.handleCloseDialogConfirm}
        handleCloseDeny={handleCloseDialog}
        isOpen={isDialogOpen}
        title={`You picked ${selectedSymptom.name}`}
      />
    );
  }

  renderDiagnoses = () => {
    const { diagnoses } = this.props;
    const totalFrequencies = diagnoses.reduce((accum, curr) => accum += curr.frequency, 0);
    return (
      <List component='nav'>
        {diagnoses.map(this.renderDiagnosis.bind(null, totalFrequencies))}
      </List>
    );
  }

  renderDiagnosesSelector = () => {
    const {
      diagnoses,
      diagnosisStatus,
      handleDiagnosisSlector,
      selectedDiagnosis,
      selectedSymptom
    } = this.props;

    const title = `Okay, let's figure this out together. Pick a cause of your symptom ${selectedSymptom.name}`;
    const newData = diagnoses.filter(item => item.id !== selectedDiagnosis.id);
    return <FullScreenDialogCompnent
      data={newData}
      handleClick={handleDiagnosisSlector}
      isOpen={diagnosisStatus === PENDING}
      title={title}
    />
  }

  render() {
    const { diagnosisStatus, handleRefresh, handleSelectChange, selectedSymptom } = this.props;
    return (
      <div>
        <AppBar position='static' className={styles.appBar}>
          <Toolbar>
            <Typography variant='h6' color='inherit'>
              Lets get you feeling better
            </Typography>
            <div className={styles.spacer} />
            <Button color='inherit' onClick={handleRefresh}>Start Over</Button>
          </Toolbar>
        </AppBar>
        <SelectComponent
          label={'Sympom Selector'}
          handleChange={handleSelectChange}
          disabled={!!selectedSymptom.id}
          selectedValue={selectedSymptom.id ? selectedSymptom : ''}
        />
        {this.renderDialog()}
        {diagnosisStatus === DETERMINED && this.renderDiagnoses()}
        {this.renderDiagnosesSelector()}
      </div>
    );
  }
}
