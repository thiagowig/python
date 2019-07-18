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
  success: boolean = false;

  displayedColumns: string[] = ['id', 'name'];
  noteTypes: NoteType[];
  isLoadingResults = false;



  constructor(
    private formBuilder: FormBuilder,
    private apiService: ApiService
  ) { }

  ngOnInit() {
    this.notesTypeForm = this.formBuilder.group({
      name: ['', Validators.required]
    });

    this.listAll();
  }

  listAll() {
    this.isLoadingResults = true;

    this.apiService.getNotesTypes().subscribe(data => {
      this.noteTypes = data.noteTypes;
      console.log(this.noteTypes);
      this.isLoadingResults = false;
    }, err => {
      console.log(err);
      this.isLoadingResults = false;
    });
  }

  onSubmit() {
    this.submitted = true;

    if (this.notesTypeForm.invalid) {
        return;
    }

    this.apiService.getNotesTypes().subscribe((res) => {
      console.log(res);
    });

    this.success = true;
  }

}
