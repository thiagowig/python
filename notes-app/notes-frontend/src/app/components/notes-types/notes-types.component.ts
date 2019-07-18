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
      console.log(this.noteTypes);
    }, err => {
      console.log(err);
    });
  }

  update(noteType: NoteType) {
    this.notesTypeForm.get("name").setValue(noteType.name);
    this.notesTypeForm.get("id").setValue(noteType.id);
  }

  onSubmit() {
    this.submitted = true;

    if (this.notesTypeForm.invalid) {
        return;
    }

    this.apiService.getNotesTypes().subscribe((res) => {
      console.log(res);
    });
  }

}
