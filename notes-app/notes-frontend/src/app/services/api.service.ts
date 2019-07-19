import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NoteTypeResponse } from '../classes/note-type-response';
import { NoteTypeWrapper } from '../classes/note-type-wrapper';
import { NoteType } from '../classes/note-type';
import { environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  apiUrl: string = `${environment.apiBaseUrl}/v1.0/noteTypes`;

  constructor(private httpClient: HttpClient) { }

  public getNotesTypes(){
    return this.httpClient.get<NoteTypeResponse>(this.apiUrl);
  }

  public saveNoteType(noteType: NoteType) {
    if (noteType.id) {
      return this.httpClient.put<NoteTypeWrapper>(`${this.apiUrl}/${noteType.id}`, noteType);

    } else {
      return this.httpClient.post<NoteTypeWrapper>(this.apiUrl, noteType);
    }
  }

  public deleteNoteType(noteType: NoteType) {
    return this.httpClient.delete<NoteTypeWrapper>(`${this.apiUrl}/${noteType.id}`);
  }
}
