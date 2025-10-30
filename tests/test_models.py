"""Tests for data models."""

from models import Course, CourseChunk, Lesson


def test_course_model():
    """Test Course model creation."""
    course = Course(id="test-1", name="Test Course", description="A test course")
    assert course.id == "test-1"
    assert course.name == "Test Course"
    assert course.description == "A test course"
    assert course.lessons == []


def test_lesson_model():
    """Test Lesson model creation."""
    lesson = Lesson(
        id="lesson-1",
        course_id="course-1",
        title="Lesson 1",
        content="Test content",
        file_path="test.txt",
    )
    assert lesson.id == "lesson-1"
    assert lesson.course_id == "course-1"
    assert lesson.title == "Lesson 1"


def test_course_chunk_model():
    """Test CourseChunk model creation."""
    chunk = CourseChunk(
        id="chunk-1",
        course_id="course-1",
        lesson_id="lesson-1",
        content="Test chunk content",
        metadata={"source": "test.txt"},
    )
    assert chunk.id == "chunk-1"
    assert chunk.course_id == "course-1"
    assert chunk.lesson_id == "lesson-1"
    assert "source" in chunk.metadata
