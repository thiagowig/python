import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators} from '@angular/forms';

@Component({
  selector: 'app-notes-types',
  templateUrl: './notes-types.component.html',
  styleUrls: ['./notes-types.component.css']
})
export class NotesTypesComponent implements OnInit {

  notesTypeForm: FormGroup;
  submitted = false;
  success: boolean = false;

  constructor(private formBuilder: FormBuilder) { }

  ngOnInit() {
    this.notesTypeForm = this.formBuilder.group({
      name: ['', Validators.required]
    });
  }

  onSubmit() {
    this.submitted = true;

    if (this.notesTypeForm.invalid) {
        return;
    }

    this.success = true;
  }

}
