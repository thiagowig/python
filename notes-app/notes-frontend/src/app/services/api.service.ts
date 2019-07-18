import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { NoteType } from '../classes/note-type';
import { environment} from '../../environments/environment';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  listAllURL: string = `${environment.apiBaseUrl}/v1.0/noteTypes`;

  constructor(private httpClient: HttpClient) { }

  public getNotesTypes(){
    return this.httpClient.get<NoteType[]>(this.listAllURL);
  }
}
