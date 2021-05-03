import { ComponentFixture, TestBed, waitForAsync } from '@angular/core/testing';

import { ParametrizacionComponent } from './parametrizacion.component';

describe('ParametrizacionComponent', () => {
  let component: ParametrizacionComponent;
  let fixture: ComponentFixture<ParametrizacionComponent>;

  beforeEach(waitForAsync(() => {
    TestBed.configureTestingModule({
      declarations: [ ParametrizacionComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ParametrizacionComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
