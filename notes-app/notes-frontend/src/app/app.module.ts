import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { HttpClientModule } from '@angular/common/http';
import { NotesMaterialModule } from './modules/notes-material/notes-material.module';

import { AppComponent } from './app.component';
import { NotesTypesComponent } from './components/notes-types/notes-types.component';
import { NoopAnimationsModule } from '@angular/platform-browser/animations';

@NgModule({
  declarations: [
    AppComponent,
    NotesTypesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    ReactiveFormsModule,
    NoopAnimationsModule,
    NotesMaterialModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
