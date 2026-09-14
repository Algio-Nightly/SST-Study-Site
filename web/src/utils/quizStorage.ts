export interface SavedQuizProgress {
  selectedAnswers: Record<string, string[]>;
  submittedQuestions: Record<string, boolean>;
  activeQuestionIndex: number;
  lastUpdated: number;
  markedDoneQuestions?: Record<string, boolean>;
  markedReviewQuestions?: Record<string, boolean>;
}

export interface LectureStudyStatus {
  isDone?: boolean;
  isReview?: boolean;
  lastUpdated?: number;
}

const STORAGE_PREFIX = 'sst_quiz_v1';
const LECTURE_STATUS_PREFIX = 'sst_notes_status_v1';

export function getQuizStorageKey(subjectId: string, lectureId: string): string {
  return `${STORAGE_PREFIX}_${subjectId}_${lectureId}`;
}

export function getSubjectLectureStatusKey(subjectId: string): string {
  return `${LECTURE_STATUS_PREFIX}_${subjectId}`;
}

export function loadAllSubjectLectureStatuses(subjectId: string): Record<string, LectureStudyStatus> {
  try {
    const key = getSubjectLectureStatusKey(subjectId);
    const raw = localStorage.getItem(key);
    if (!raw) return {};
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed === 'object') {
      return parsed as Record<string, LectureStudyStatus>;
    }
  } catch (err) {
    console.warn(`[QuizStorage] Failed to load lecture statuses for ${subjectId}:`, err);
  }
  return {};
}

export function loadLectureStatus(subjectId: string, lectureId: string): LectureStudyStatus {
  const all = loadAllSubjectLectureStatuses(subjectId);
  return all[lectureId] || { isDone: false, isReview: false };
}

export function saveLectureStatus(
  subjectId: string,
  lectureId: string,
  status: Partial<LectureStudyStatus>
): Record<string, LectureStudyStatus> {
  try {
    const all = loadAllSubjectLectureStatuses(subjectId);
    all[lectureId] = {
      ...(all[lectureId] || { isDone: false, isReview: false }),
      ...status,
      lastUpdated: Date.now()
    };
    const key = getSubjectLectureStatusKey(subjectId);
    localStorage.setItem(key, JSON.stringify(all));
    return all;
  } catch (err) {
    console.warn(`[QuizStorage] Failed to save lecture status for ${subjectId}/${lectureId}:`, err);
    return {};
  }
}

export function loadQuizProgress(subjectId: string, lectureId: string): SavedQuizProgress | null {
  try {
    const key = getQuizStorageKey(subjectId, lectureId);
    const raw = localStorage.getItem(key);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (parsed && typeof parsed.selectedAnswers === 'object') {
      return parsed as SavedQuizProgress;
    }
  } catch (err) {
    console.warn(`[QuizStorage] Failed to parse quiz progress for ${subjectId}/${lectureId}:`, err);
  }
  return null;
}

export function saveQuizProgress(
  subjectId: string, 
  lectureId: string, 
  progress: SavedQuizProgress
): void {
  try {
    const key = getQuizStorageKey(subjectId, lectureId);
    localStorage.setItem(key, JSON.stringify(progress));
  } catch (err) {
    console.warn(`[QuizStorage] Failed to save quiz progress for ${subjectId}/${lectureId}:`, err);
  }
}

/**
 * Explicitly clears quiz progress from browser local storage.
 * Per requirement: This is strictly called only when the user clicks the "Clear All" button.
 */
export function clearQuizProgress(subjectId: string, lectureId: string): void {
  try {
    const key = getQuizStorageKey(subjectId, lectureId);
    localStorage.removeItem(key);
  } catch (err) {
    console.warn(`[QuizStorage] Failed to clear quiz progress for ${subjectId}/${lectureId}:`, err);
  }
}

/**
 * Calculates aggregate stats across all lectures in a subject for dashboard display
 */
export function getSubjectProgressSummary(subjectId: string, lectureIds: string[]): {
  answeredQuestions: number;
  submittedQuestions: number;
} {
  let answered = 0;
  let submitted = 0;

  try {
    for (const lectureId of lectureIds) {
      const state = loadQuizProgress(subjectId, lectureId);
      if (state) {
        if (state.selectedAnswers) {
          answered += Object.keys(state.selectedAnswers).filter(
            k => state.selectedAnswers[k] && state.selectedAnswers[k].length > 0
          ).length;
        }
        if (state.submittedQuestions) {
          submitted += Object.keys(state.submittedQuestions).filter(
            k => state.submittedQuestions[k] === true
          ).length;
        }
      }
    }
  } catch (e) {
    console.warn('[QuizStorage] Error reading subject summary:', e);
  }

  return {
    answeredQuestions: answered,
    submittedQuestions: submitted
  };
}
