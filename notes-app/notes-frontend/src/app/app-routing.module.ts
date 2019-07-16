import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { NotesTypesComponent } from './components/notes-types/notes-types.component'; 


const routes: Routes = [
  {
    path: 'types',
    component: NotesTypesComponent
  }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
