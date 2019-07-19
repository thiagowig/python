import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';
import { ApiService } from '../../services/api.service';
import { NoteType } from '../../classes/note-type';


@Component({
  selector: 'app-notes-types',
  templateUrl: './notes-types.component.html',
  styleUrls: ['./notes-types.component.css']
})
export class NotesTypesComponent implements OnInit {

  notesTypeForm: FormGroup;
  submitted = false;

  noteTypes: NoteType[];
  noteType: NoteType = new NoteType();

  constructor(
    private formBuilder: FormBuilder,
    private apiService: ApiService
  ) { }

  ngOnInit() {
    this.notesTypeForm = this.formBuilder.group({
      name: ['', Validators.required],
      id: ['']
    });

    this.listAll();
  }

  listAll() {
    this.apiService.getNotesTypes().subscribe(data => {
      this.noteTypes = data.noteTypes;
      this.sortList();
      console.log(this.noteTypes);
    }, err => {
      console.log(err);
    });
  }

  sortList() {
    this.noteTypes.sort((a, b) => {
      return (a.name < b.name) ? -1 : (a.name > b.name) ? 1 : 0;
    })
  }

  update(noteType: NoteType) {
    this.notesTypeForm.get("name").setValue(noteType.name);
    this.notesTypeForm.get("id").setValue(noteType.id);
  }

  delete(noteType: NoteType) {
    this.apiService.deleteNoteType(noteType).subscribe((res) => {
      console.log(res);
      var elementIndex = this.noteTypes.indexOf(noteType);
      this.noteTypes.splice(elementIndex, 1);
      this.sortList();
    }, err => {
      console.log(err);
    });
  }

  saveNoteType() {
    this.submitted = true;

    if (this.notesTypeForm.invalid) {
        return;
    }

    this.apiService.saveNoteType(this.notesTypeForm.value).subscribe((res) => {
      this.notesTypeForm.get("name").setValue(res.noteType.name);
      this.notesTypeForm.get("id").setValue(res.noteType.id);

      var elementIndex = this.noteTypes.indexOf(this.notesTypeForm.value);
      this.noteTypes.splice(elementIndex, 1);
      this.noteTypes.push(res.noteType);
      this.sortList();
    }, err => {
      console.log(err);
    });
  }

  newNoteType() {
    this.notesTypeForm.reset();
  }

}
