import { TestBed } from '@angular/core/testing';

import { ApiConenctionService } from './api-conenction.service';

describe('ApiConenctionService', () => {
  let service: ApiConenctionService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ApiConenctionService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
