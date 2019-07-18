import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NoteType } from '../classes/note-type';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  apiURL: string = 'https://notes-python-gcp.appspot.com/api/v1.0/noteTypes';

  constructor(private httpClient: HttpClient) { }

  public getNotesTypes(){
    console.log('Calling the API');
    return this.httpClient.get<NoteType[]>(this.apiURL);
  }
}
