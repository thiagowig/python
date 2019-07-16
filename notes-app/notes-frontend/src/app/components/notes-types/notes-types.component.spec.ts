import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { NotesTypesComponent } from './notes-types.component';

describe('NotesTypesComponent', () => {
  let component: NotesTypesComponent;
  let fixture: ComponentFixture<NotesTypesComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ NotesTypesComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(NotesTypesComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
