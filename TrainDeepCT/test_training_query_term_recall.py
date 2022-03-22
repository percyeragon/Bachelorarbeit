import json
import importlib
calculate_doc_term_recall = importlib.import_module('get_training_query_term_recall').calculate_doc_term_recall
passage_calculate_doc_term_recall = importlib.import_module('passage_extraction_util').passage_calculate_doc_term_recall


class test_args():
    def stem():
        return True
        
    def stop():
        return True


def test_small_document():
    input_data = ['{"queries": ["what kind of animals are in grasslands", "tropical grasslands animals"], "doc":{"title": "Tropical grassland animals (which do not all occur in the same area)."}}']
    expected = [{"doc": {"title": "Tropical grassland animals (which do not all occur in the same area).", "position": 1, "id": 1}, "term_recall": {"tropical": 0.5, "grassland": 1.0, "animals": 1.0}}]
    actual = [i for i in calculate_doc_term_recall(input_data, test_args())]

    assert expected == actual


def test_small_document_with_stemming():
    # different flections of animal(s) are mapped to the same term
    input_data = ['{"queries": ["what kind of animal are in grasslands", "tropical grasslands animals"], "doc":{"title": "Tropical grassland animals (which do not all occur in the same area)."}}']
    expected = [{"doc": {"title": "Tropical grassland animals (which do not all occur in the same area).", "position": 1, "id": 1}, "term_recall": {"tropical": 0.5, "grassland": 1.0, "animals": 1.0}}]

    actual = [i for i in calculate_doc_term_recall(input_data, test_args())]

    assert expected == actual

def test_small_document_with_stemming_and_passages():
    # different flections of animal(s) are mapped to the same term
    input_data = ['{"queries": ["what kind of animal are in grasslands", "tropical grasslands animals"], "doc":{"title": "Tropical grassland animals (which do not all occur in the same area)."}}']
    expected = [{"doc": {"title": "Tropical grassland animals (which do not all occur in the same area).", "position": 1, "id": 1}, "term_recall": {"tropical": 0.5, "grassland": 1.0, "animals": 1.0}}]

    actual = [i for i in passage_calculate_doc_term_recall(input_data, test_args())]

    assert expected == actual

def test_multi_passage_document_with_stemming_and_passages():
    # different flections of animal(s) are mapped to the same term
    input_data = ['{"queries": ["what kind of animal are in grasslands", "tropical grasslands animals"], "doc":{"title": "Tropical grassland animals (which do not all occur in the same area). This is a stupid sentence. This is also a stupid sentence. This is a stupid sentence. This is a stupid sentence. This is a stupid sentence. This is also a stupid sentence. This is a stupid sentence. This is a stupid sentence with animals."}}']
    expected = [{'doc': {'title': 'Tropical grassland animals (which do not all occur in the same area). This is a stupid sentence. This is also a stupid sentence. This is a stupid sentence. This is a stupid sentence. This is a stupid sentence. This is also a stupid sentence. This is a stupid sentence. ', 'position': 1, 'id': 1}, 'term_recall': {'animals': 1.0, 'grassland': 1.0, 'tropical': 0.5}}, {'doc': {'title': 'This is a stupid sentence with animals.', 'position': 1, 'id': 1}, 'term_recall': {'animals': 1.0}}]

    actual = [i for i in passage_calculate_doc_term_recall(input_data, test_args())]

    print(actual)
    assert expected == actual

